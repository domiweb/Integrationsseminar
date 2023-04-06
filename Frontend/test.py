import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """
        <html>
            <head>
                <title>Hello World</title>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
                <script>
                    $(document).ready(function() {
                        $('#submit').click(function() {
                            var userInput = $('#user-input').val();
                            $.ajax({
                                type: 'POST',
                                url: '/process_input',
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
                <h1>Hello World</h1>
                <input id="user-input" type="text">
                <button id="submit">Submit</button>
            </body>
        </html>
        """

    @cherrypy.expose
    def process_input(self, user_input):
        # Hier können Sie die Nutzereingabe verarbeiten
        return 'Nutzereingabe: {}'.format(user_input)

if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())
