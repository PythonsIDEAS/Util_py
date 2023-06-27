import os
import shutil

# Путь к каталогу "Видео"
video_directory = "C:\Видео"

# Путь к каталогу "Видео/исходники"
source_directory = os.path.join(video_directory, "исходники")

# Путь к каталогу "Видео/превью"
preview_directory = os.path.join(video_directory, "превью")

# Путь к каталогу "Видео/аудио"
audio_directory = os.path.join(video_directory, "аудио")

# Путь к каталогу "Видео/видео"
video_files_directory = os.path.join(video_directory, "видео")

# Создаем каталоги, если они не существуют
if not os.path.exists(source_directory):
    os.makedirs(source_directory)
if not os.path.exists(preview_directory):
    os.makedirs(preview_directory)
if not os.path.exists(audio_directory):
    os.makedirs(audio_directory)
if not os.path.exists(video_files_directory):
    os.makedirs(video_files_directory)

# Перебираем файлы в каталоге "Видео"
for filename in os.listdir(video_directory):
    file_path = os.path.join(video_directory, filename)

    # Проверяем, является ли файл расширением .mkv, .mov, .psd или .mp3
    if filename.endswith(".mkv") or filename.endswith(".mov"):
        # Перемещаем файл в каталог "Видео/исходники"
        shutil.move(file_path, source_directory)
    elif filename.endswith(".psd"):
        # Перемещаем файл в каталог "Видео/превью"
        shutil.move(file_path, preview_directory)
    elif filename.endswith(".mp3"):
        # Перемещаем файл в каталог "Видео/аудио"
        shutil.move(file_path, audio_directory)
    elif filename.endswith(".mov"):
        # Перемещаем файл в каталог "Видео/видео"
        shutil.move(file_path, video_files_directory)
    else:
        # Оставляем файл в текущем каталоге
        pass