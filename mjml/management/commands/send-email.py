import json
from django.core.management import BaseCommand
from django.template.loader import render_to_string

from mjml.utils import (
    transpile_mjml_to_html,
    get_context_for_template,
    send_email,
)


class Command(BaseCommand):
    help = 'transpile, process and send mjml email'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, file_name, *args, **options):
        # transpile mjml to html
        success = transpile_mjml_to_html(file_name)
        if not success:
            self.stdout.write(self.style.ERROR('MJML transpilation failed'))
            return
        self.stdout.write(self.style.SUCCESS('MJML transpilation successful'))

        # load context from json
        context = get_context_for_template(file_name)
        self.stdout.write(self.style.SUCCESS(f'Context loaded: {json.dumps(context, indent=2)}'))

        # process template
        template_name = 'email/' + file_name + '.html'
        email_message = render_to_string(template_name, context)

        # send email
        mail_settings = send_email(email_message, file_name)
        self.stdout.write(self.style.SUCCESS(f'Email sent to {mail_settings.get("recipients")}'))


