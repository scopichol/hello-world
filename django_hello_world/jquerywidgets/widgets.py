from django.forms import DateInput
from django.utils.safestring import mark_safe

class CalendarWidget(DateInput):
    def render(self, name, value, attrs=None):
        print '\n'.join(dir(self)
        script= '\n<script>$(function() {$.datepicker.setDefaults({dateFormat: "yy-mm-dd"});$( "#id_birthday" ).datepicker();});</script>'
        input = super(CalendarWidget, self).render( name, value, attrs)

        return mark_safe(input + script)
    
    class Media:
        css = {
            'all': ('http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/themes/base/jquery-ui.css',)
        }
