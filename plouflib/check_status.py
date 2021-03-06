from plouflib.http import HTTPRequest

class StatusCheck:

    def __init__(self,options):
        self.options = options

    def headers(self):
        return ['Status code','Redirection URL','Status code','Redirection URL']

    def process(self,request):
        if request.status == 301 or request.status == 302:
            subrequest = HTTPRequest(request.get_location())
            subrequest.get_headers()
            return [str(request.status), request.get_location(), str(subrequest.status), subrequest.get_location()]
        else :
            return [str(request.status), request.get_location(), '', '']
