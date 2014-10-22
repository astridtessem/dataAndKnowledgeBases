var counter =0;
Template.fix.events({
	'keypress .input': function(event,t) {
        if (event.charCode == 49) {
           	Meteor.call('update','O',counter)
        }
        if (event.charCode == 50) {
           	Meteor.call('update','P',counter)
        }
        if (event.charCode == 51) {
           	Meteor.call('update','OR',counter)
        }
        if(event.charCode==52){
        	Meteor.call('update','D',counter)
        }
        if(event.charCode==53){
        	Meteor.call('update','N',counter)
        }
        if(event.charCode==54){
        	Meteor.call('update','L',counter);
        }
        counter = counter +1;
        
    }
})
Template.fix.wordList = function(){
	Session.set("selected_word",this._id);
	return InputText.findOne({e:""})
}