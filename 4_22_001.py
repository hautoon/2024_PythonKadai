from PIL import Image, ImageDraw

def crop_circle(image_path, output_path):
  """
  画像の中心から円形に画像を切り取り、指定のパスに出力します。

  Args:
    image_path: 入力画像のパス
    output_path: 出力画像のパス
  """
  # 画像を読み込む
  image = Image.open(image_path)

  # 画像の幅と高さを取得する
  width, height = image.size

  # 縁の半径を計算する
  radius = width // 4

  # 円の中心を計算する
  center_x = width // 2
  center_y = height // 2

  # 左上と右下の座標を計算する
  top_left_x = center_x - radius
  top_left_y = center_y - radius
  bottom_right_x = center_x + radius
  bottom_right_y = center_y + radius

  # 円形に切り取る
  cropped_image = image.crop((top_left_x, top_left_y, bottom_right_x, bottom_right_y))
  # 新しい画像を作成（透過可能にするためにRGBAモードを使用）
  circle_img = Image.new('RGBA', (width, height))
  draw = ImageDraw.Draw(circle_img)

  # 中心点を計算
  center_x, center_y = width // 2, height // 2

  # 円形のマスクを描く
  draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=(255, 255, 255, 255))

  # 元の画像とマスクを合成
  result = Image.alpha_composite(Image.new('RGBA', image.size, (255, 255, 255, 0)), circle_img)
  result.putalpha(circle_img.split()[-1])  # アルファチャンネルを使用してマスク適用

  # 切り取った画像を重ねる
  circle_cropped_img = Image.new('RGBA', (2 * radius, 2 * radius), (255, 255, 255, 0))
  circle_cropped_img.paste(result, (-center_x + radius, -center_y + radius), result)

  # 出力画像を保存する
  cropped_image.save(output_path)

# 例
image_path = "input.jpeg"
output_path = "output.png"
crop_circle(image_path, output_path)