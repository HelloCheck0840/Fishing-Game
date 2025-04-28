text = "A very"

line_length = 20
lines = [text[i:i+20] + '\n' for i in range(0, len(text), line_length)]
text = ''.join(lines)
print(text)