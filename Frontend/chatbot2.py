import cherrypy
import chatbot_model
#from chatbot_model import predict_class, get_response, dataf



cherrypy.config.update({'server.socket_port': 8099})


class Chatbot(object):

	@cherrypy.expose
	def index(self):
		return '''
            <html>

<head>

	<!-- seo related -->
	<title>Chatbot Frontend</title>

	<!-- meta related -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />

	<!-- vendor css & style files -->
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
	<link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300|Open+Sans:300|Oxygen|Material+Icons"
		rel="stylesheet">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">

	<script src="https://code.jquery.com/jquery-2.2.4.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>

	<!-- custom css -->
	<link rel="stylesheet" type="text/css" href="static/main.css">

	<script>
		$(document).ready(function() {
			$('#send_button').click(function() {
				var userInput = $('#msg_input').val();
				$.ajax({
	type: 'POST',
	url: '/submit',
	data: { user_input: userInput },
	dataType: 'text',
	success: function(response) {
	alert(response);
	// Hier können Sie Ihre JS-Funktion aufrufen
	},
	error: function() {
	alert('An error occurred.');
	}
	});
	$('#user-input').val('');
	});
	});
	</script>


</head>

<body>

	<div class="container">

		<div class="row padded_row">

			<!-- right side content -->
			<div class="col-md-7">

				<div class="chat_window">

					<div class="top_menu">
						<div class="title">ChatBot - Jarvis</div>
					</div>

					<!-- dynamically rendered -->
					<ul class="messages"></ul>

					<!-- input -->
					<div class="bottom_wrapper">
						<input id="msg_input" placeholder="Say Hi to begin chat..." />
						<button id="send_button" class="app_button_1">Send</button>
					</div>

				</div>

			</div>

			<!-- left side content -->
			<div class="col-md-5">
				<div class="chat_window">

					<div class="top_menu">
						<div class="title">Help</div>
					</div>

					<!-- help container -->
					<div class="panel-group" id="accordion">

						<!-- help - 1 -->
						<div class="panel panel-default">
							<div class="panel-heading">
								<h4 class="panel-title">
									<a class="accordion-toggle" data-toggle="collapse" data-parent="#accordion"
										href="#collapse1">Lorem ipsum</a>
								</h4>
							</div>
							<div id="collapse1" class="panel-collapse collapse in">
								<div class="panel-body">
									Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
									mollit anim id est laborum
								</div>
							</div>
						</div>

					</div>

				</div>
			</div>

		</div>

	</div>

	<!-- vendor script files -->


	<!-- custom scripts -->
	<script src="static/main.js"></script>
</body>

</html>

        '''

	@cherrypy.expose
	def submit(self, user_input):

		ints = chatbot_model.predict_class(user_input)
		res = chatbot_model.get_response(ints, chatbot_model.data)

		# return message

		return res


if __name__ == '__main__':
	cherrypy.quickstart(Chatbot())
