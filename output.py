import json
import os

if __name__ == "__main__":
    with open("data.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    content_dir, reports = "content", []
    for item in os.listdir(os.getcwd() + os.sep + content_dir):
        reports.append(dict(title=item, href=content_dir + os.sep + item))
    config["reports"] = reports

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
