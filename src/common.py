def get_file_content(file_path, n=None):
    """
    将enums.py文本输出
    :return:
    """
    with open(file_path, "r") as f:
        if n:
            content = ""
            for _ in range(n):
                content += f.readline()
        else:
            content = f.read()
    return "\n" + content

