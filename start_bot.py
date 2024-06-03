import asyncio
import logging
import sys


from service_tg import main

logging.basicConfig(level=logging.INFO, stream=sys.stdout)
asyncio.run(main())
