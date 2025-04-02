from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    """
    Encrypt an image by performing pixel manipulation
    """
    try:
        # Open the image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Perform encryption operations
        # 1. Swap color channels (R <-> B)
        encrypted_pixels = pixels.copy()
        encrypted_pixels[:, :, [0, 2]] = encrypted_pixels[:, :, [2, 0]]
        
        # 2. Apply XOR operation with key to each pixel component
        encrypted_pixels = encrypted_pixels ^ (key % 256)
        
        # 3. Flip the image vertically
        encrypted_pixels = np.flipud(encrypted_pixels)
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path, key):
    """
    Decrypt an image by reversing the pixel manipulation
    """
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Reverse the encryption operations
        # 1. Flip the image vertically (undoing the flip)
        decrypted_pixels = np.flipud(pixels)
        
        # 2. Apply XOR operation with key (same as encryption)
        decrypted_pixels = decrypted_pixels ^ (key % 256)
        
        # 3. Swap color channels back (B <-> R)
        decrypted_pixels[:, :, [0, 2]] = decrypted_pixels[:, :, [2, 0]]
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
        
    except Exception as e:
        print(f"Error during decryption: {e}")

def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    choice = input("Enter your choice (1/2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice")
        return
    
    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    try:
        key = int(input("Enter encryption key (integer): "))
    except ValueError:
        print("Key must be an integer")
        return
    
    if choice == '1':
        encrypt_image(input_path, output_path, key)
    else:
        decrypt_image(input_path, output_path, key)

if name == "main":
    main()