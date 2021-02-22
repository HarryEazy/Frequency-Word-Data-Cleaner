
import re


raw_string = stringy = """"""""

pattern = r"[0-9]"
mod_string = re.sub(pattern, "", stringy)
print(mod_string)