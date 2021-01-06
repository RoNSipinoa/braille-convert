import asyncio

async def braille_decompose():
    a = ord(input('which braille to decompose?:    ')) - 10240
    output_string = ''
    for i in range(8, 0, -1):
        if a - 2 ** (i - 1) >= 0:
            output_string = str(i) + output_string
            a -= 2 ** (i - 1)
        else:
            pass
    print(output_string)
    
asyncio.run(braille_decompose)
