import click

from theboard import app, db
from theboard.models import Message

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after dorp.')
def initdb(drop):
    """ initialize the database. """
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
@click.option('--count', default=1, help='Quantity of messages, default is 1.')
def pre(count):
    """ Generate fake messages. """
    from faker import Faker

    db.drop_all()
    db.create_all()

    fake = Faker()
    click.echo('🛠-Generating...')
    for i in range (count):
        message = Message(
            name = fake.name(),
            body = fake.sentence(),
            timestamp = fake.date_time_this_year()
        )
        db.session.add(message)
    
    db.session.commit()
    click.echo('Done! Created %d fake messages.' %count)