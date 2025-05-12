import os

def remove_zone_identifier_files(directory):
  count = 0
  for root, _, files in os.walk(directory):
    for filename in files:
      if 'Zone.Identifier' in filename:
        file_path = os.path.join(root, filename)
        try:
          os.remove(file_path)
          print(f"Removed: {file_path}")
          count += 1
        except Exception as e:
          print(f"Error removing {file_path}: {e}")
  print(f"Removed {count} 'Zone.Identifier' files.")

if __name__ == '__main__':
  dataset_path = './dataset'  # Replace with your dataset directory
  remove_zone_identifier_files(dataset_path)