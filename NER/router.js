Router.map(function() {
	this.route('home', {path: '/'});
	this.route('fix');
});

Router.configure({
	layoutTemplate: 'layout'
});

