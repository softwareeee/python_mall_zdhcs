import re

def replace_global(string, global_vars):
    pattern = r'{{\w+}}'  # 正则表达式匹配形如 {{variable}} 的格式
    for var in re.findall(pattern, string):
        if var[2:-2] in global_vars:
            value = global_vars[var[2:-2]]
            string = string.replace(var, str(value))
    return string