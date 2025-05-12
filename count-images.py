import os

def count_files(directory_path):
  """Counts the total number of files (excluding subdirectories)
  within a given directory.

  Args:
    directory_path: The path to the directory you want to count files in.

  Returns:
    An integer representing the total number of files in the directory,
    or None if the path is not a valid directory.
  """
  if not os.path.isdir(directory_path):
    print(f"Error: '{directory_path}' is not a valid directory.")
    return None

  file_count = 0
  for item in os.listdir(directory_path):
    item_path = os.path.join(directory_path, item)
    if os.path.isfile(item_path):
      file_count += 1
  return file_count

if __name__ == '__main__':
  directory_to_count = './dataset'  # Replace with the actual path to your dataset directory
  total_files = count_files(directory_to_count)
  if total_files is not None:
    print(f"Total number of files in '{directory_to_count}': {total_files}")

  # If your images are in subdirectories (which they should be for your setup),
  # you'll need to count files recursively. Here's how:

  def count_files_recursive(directory_path):
    """Counts the total number of files (excluding subdirectories)
    within a given directory and its subdirectories.

    Args:
      directory_path: The path to the directory you want to count files in.

    Returns:
      An integer representing the total number of files.
      Returns 0 if the path is not a valid directory.
    """
    total_files = 0
    if not os.path.isdir(directory_path):
      print(f"Error: '{directory_path}' is not a valid directory.")
      return 0

    for root, _, files in os.walk(directory_path):
      total_files += len(files)
    return total_files

  total_images = count_files_recursive(directory_to_count)
  print(f"Total number of images in '{directory_to_count}' (including subdirectories): {total_images}")