# Compiled By Mr Mafia | YOUCEF HAFAFNI
# Github :  https://github.com/MAFIAT2

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
