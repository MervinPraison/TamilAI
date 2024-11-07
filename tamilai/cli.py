import click
from .translator import TamilAI

@click.command()
@click.argument('question', nargs=-1)
def main(question):
    """TamilAI - An AI assistant that responds in Tamil"""
    if not question:
        click.echo("Please provide a question.")
        return
    
    # Join multiple words into a single question
    full_question = ' '.join(question)
    
    ai = TamilAI()
    response = ai.get_response(full_question)
    click.echo(response)

if __name__ == '__main__':
    main() 