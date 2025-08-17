input_text = input("")
allowed_chars = "abcdefghijklmnopqrstuvwxyz "
lower_text_stage = input_text.lower()
cleaned_text_stage = ""
for ch in lower_text_stage:
    if ch not in allowed_chars:
        cleaned_text_stage += " "
    else:
        cleaned_text_stage += ch
title_text_stage = cleaned_text_stage.title()

split_text_stage = title_text_stage.split()

join_text_stage = "".join(split_text_stage)

limited_text_stage = join_text_stage[:140]
final_hashtag = "#" + limited_text_stage
print(final_hashtag)