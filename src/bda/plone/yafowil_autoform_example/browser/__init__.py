from Products.Five import BrowserView


class YafowilExampleView(BrowserView):

    def __init__(self, context, request):
        super(YafowilExampleView, self).__init__(context, request)
        print(80 * '#')
