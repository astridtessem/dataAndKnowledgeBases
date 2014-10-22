InputText = new Meteor.Collection("inputText");
ProcessedText = new Meteor.Collection("processedText");
Meteor.subscribe('inputText');
Meteor.subscribe('processedText');

Template.home.events({
	'click .inputBtn':function(e,t){
		var text = t.find('.inputText').value;
		//Meteor.call('addText',text);
		Meteor.call('callPython',text);
	},
	'click .resetBtn':function(){
		Meteor.call('reset');
	}
})

Template.home.textList = function(){
	//return InputText.find({},{sort:{i:1}});
	return InputText.find({})
}
Template.home.entityList = function(){
	//return InputText.find({},{sort:{i:1}});
	return ProcessedText.find({});
}
Template.home.totalList = function(){
	var text =  InputText.find().fetch();
	var ptext = ProcessedText.find().fetch();
	var docs = text.concat(ptext);
	return docs;
}
