import re
import socket


def identify_host():
    """Function to determine which host the client is running from.
    """
    cheyenne = re.compile(r'cheyenne')
    casper = re.compile(r'casper')
    hobart = re.compile(r'hobart')

    hostname = socket.getfqdn()

    is_on_cheyenne = cheyenne.search(hostname)
    is_on_casper = casper.search(hostname)
    is_on_hobart = hobart.search(hostname)

    try:
        if is_on_cheyenne:
            return 'cheyenne'

        elif is_on_casper:
            return 'casper'

        elif is_on_hobart:
            return 'hobart'

        else:
            raise RuntimeError(
                'Unable to determine which NCAR cluster you are running on...'
            )

    except Exception as exc:
        raise exc('Unable to determine which NCAR cluster you are running on...')