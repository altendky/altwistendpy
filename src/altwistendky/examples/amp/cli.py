import attr
import click
import twisted.internet.defer

import altwistendky.examples.amp.client
import altwistendky.examples.amp.server


@attr.s
class ContextObject:
    reactor = attr.ib()


@click.group()
@click.pass_context
def cli(context):
    import twisted.internet.reactor

    twisted.internet.defer.setDebugging(True)

    context.obj = ContextObject(
        reactor=twisted.internet.reactor,
    )


@cli.command()
@click.pass_obj
def serve(context):
    altwistendky.examples.amp.server.serve(reactor=context.reactor)
    context.reactor.run()


@cli.command()
@click.option('--text', required=True)
@click.pass_obj
def connect(context, text):
    d = altwistendky.examples.amp.client.client(
        reactor=context.reactor,
        text=text,
    )
    d.addErrback(twisted.python.log.err, "Connection failed")
    d.addCallback(lambda _: context.reactor.stop())
    context.reactor.run()
