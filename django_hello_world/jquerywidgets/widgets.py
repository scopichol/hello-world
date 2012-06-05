from django.forms import DateInput
from django.utils.safestring import mark_safe

class CalendarWidget(DateInput):
    def __init__(self, attrs=None, format=None):
        super(CalendarWidget, self).__init__(attrs, format)
        jq_format = self.format
        jq_format = jq_format.replace('%Y','yy')
        jq_format = jq_format.replace('%y','y')
        jq_format = jq_format.replace('%m','mm')
        jq_format = jq_format.replace('%b','M')
        jq_format = jq_format.replace('%B','MM')
        jq_format = jq_format.replace('%d','dd')
        self.jq_format = jq_format
        
    def render(self, name, value, attrs=None):
        script= '\n<script>$(function(){$( "#%s" ).datepicker({dateFormat: "%s"});});</script>'%(attrs['id'], self.jq_format)
        input = super(CalendarWidget, self).render( name, value, attrs)
        
        return mark_safe(input+script)
