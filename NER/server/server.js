InputText = new Meteor.Collection("inputText");
ProcessedText = new Meteor.Collection("processedText");
Meteor.publish('inputText',function(){
	return InputText.find({});
})
Meteor.publish('processedText',function(){
	return ProcessedText.find({});
})
Meteor.methods({
	'callPython':function(text){
		//Adding the text to the inputText collection
		Meteor.call('addText',text);

		//Run the python script with the "text" as the argurment
    	var exec = Npm.require('child_process').exec;
		var Fiber = Npm.require('fibers');


		new Fiber(function(){
			//Change the directory where the python script is
			process.chdir('D:/Dropbox/NTNU/Utvikling/Meteor/Oktober/NER/server/python/');
			//The argument: script, method, attributes
		  	exec("runModel main "+text, Meteor.bindEnvironment(function (error, stdout, stderr) {
		  		var s = stdout;
		  		//Insert the python result into mongodb
		  		ProcessedText.insert({entity:s})
		  		
		  }));
		}).run();	
	},
	//Delete all the documents in the collection
	'reset':function(e,t){
		ProcessedText.remove({});
		InputText.remove({});
	},
	//Split the text into words and add them to the collection
	'addText':function(text){
		var splitText = text.replace(/\./g, "").replace(/,/g, "").split(" ");
		var i =0;
		splitText.forEach(function(entry) {
			
			InputText.insert({word:entry,e:"",i:i});
			i=i+1;
		});
	}
	// 'mergeText':function(e,t){
	// 	var textCursor = InputText.find({});
	// 	var text;
	// 	while ( raceCursor.hasNext() ) {
	// 	    race = raceCursor.next();
	// 	    console.log( race.raceName );
	// 	}
	// }
})
