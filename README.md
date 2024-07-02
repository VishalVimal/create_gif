# **Create a GIF with Python**
> Do you pronounce it “GIF” or a “JIF”? Either way, Graphics Interchange Format (GIF) is great for creating animated images. The format has been around since 1987 and helped define the early internet. It’s used to display memes, graphics, logos, and it's everywhere — on websites, text messages, and social media.

> **GIFs are “animated images” because they aren’t exactly videos. They are more like flipbooks; they don’t have sound and flip through multiple pictures sequentially.**

![gif](https://github.com/VishalVimal/create_gif/assets/89790963/b3d3e7b2-2429-4349-a06f-88b3d2197185) 

## Here’s a preview of the project:

<img src="https://github.com/VishalVimal/create_gif/assets/89790963/87be7318-8163-4be7-adab-102b00642cd9" width="300" height="400" alt="nightlife">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/8d4918a7-3877-493b-8698-eb95b92466db" width="300" height="400" alt="evening">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/410129fb-fc16-422e-a526-285833848bed" width="300" height="400" alt="cow">

## Alright, let's get started! ^ ^

# ImageIO Library
> [Imageio](https://imageio.readthedocs.io/en/stable/ "imageio link") is a Python library that provides an easy interface to read and write a wide range of image data. It runs on Python 3.5 and above.

> Suppose you have Python and pip the package installer on your computer. In that case, you can install imageio using this command in the Terminal (Mac) or Command Prompt (Windows):
``` bash
pip3 install imageio
```
Press [enter], and this message should appear:
```bash
Successfully installed imageio-2.19.3
```
Note: If you don't have Python and pip installed, make sure to go through this project.

You can quickly check if the [imageio] package was successfully installed by opening Python IDLE and running the command [import imageio]. If no errors appear, then you are good to go!

## Writing the Program

Let’s open up a code editor like VS Code and create a new file called create_gif.py.

To use the imageio library, you need to import it in your code: 
```bash
import imageio.v3 as iio
```
The "v3" in the import statement means you're using version 3 of the imageio library. The as part allows you to give the library a shorter name to work with (a nickname/alias), making it more convenient. So we've renamed imageio.v3 to iio moving forward.

Now, run the code to make sure it works. Hopefully there's no error!

Here are two images that you can use for this project:
  * [night_city1](https://github.com/VishalVimal/create_gif/assets/89790963/cb0c02ff-b4c2-48eb-b61c-48646e629a9a).png
  * [team-pic2](https://github.com/VishalVimal/create_gif/assets/89790963/db15c57c-748b-4d9f-bf98-4e380d33f917).png
Note: Make sure to store the image files in the same folder as your Python program file. 💡

In our Python program, we'll create a list that contains the locations of the image files. We also need to create an empty list that will be used to store the actual image data from these files.
```bash
filenames = ['team-pic1.png', 'team-pic2.png']
images = [ ]
```

Next, let’s use a _for_ loop to go through the file paths and read the images using _imageio_ library’s _.imread()_ method:
```bash
for filename in filenames:
  images.append(iio.imread(filename))
```

The _.imread()_ method loads an image based on the file path. So now, our _images_ variable has all the images!

Lastly, let’s use the _.imwrite()_ method to turn the images into a GIF:
```bash
iio.imwrite('team.gif', images, duration = 500, loop = 0)
```

This takes in four arguments:

  * _'team.gif'_: This is the name you want to give to your new GIF file.
  * _images_: The list containing the image data.
  * _duration_ = 500: How long each picture should show in the GIF, in milliseconds.
  * _loop_ = 0: How many times the GIF should repeat (0 means it keeps looping forever).

  And that’s it! Here’s the whole program:
  ```bash
  import imageio.v3 as iio

filenames = ['night_city1.png', 'night_city2.png']
images = [ ]

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('nightcity.gif', images, duration = 500, loop = 0)
```
You can use folders to save images.

## Running the Program
> Let’s run this program and see what happens!

> In the terminal, navigate to the folder with the Python file using cd (change directory as taught in Command Line. For example, if your file and images are in the Desktop folder, you can do:
>
```bash
cd Desktop
```

Run _python3_ and the file name: 
```bash
python3 create_gif.py
```
If you are in VS Code, you can run the program by clicking the play button ▶️ (might need to also "Select Interpreter" to run the correct version of Python).

 
A new nightcity.gif should appear in the same folder:

<img src="https://github.com/VishalVimal/create_gif/assets/89790963/87be7318-8163-4be7-adab-102b00642cd9" width="300" height="400" alt="nightlife">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/8d4918a7-3877-493b-8698-eb95b92466db" width="300" height="400" alt="evening">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/410129fb-fc16-422e-a526-285833848bed" width="300" height="400" alt="cow">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/43f96607-964d-4a53-89e5-f2a22d70770c" width="300" height="400" alt="leaf"> 
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/6f5df9b5-3e97-4fb6-b538-2980b8a35bb0" width="300" height="400" alt="rose">
<img src="https://github.com/VishalVimal/create_gif/assets/89790963/dc86beb0-aae2-44b2-ad6c-3b821dca872e" width="300" height="400" alt="nature">  

# Wrapping Up
> Congrats! You created a GIF in just 6 lines of code. Now you don’t have to rely on paid online tools to sew your images into GIFs. You just need a list, a for loop, and the _imageio_ library to do the trick. ✨

## More Resources

[Imageio Documentation](https://imageio.readthedocs.io/en/stable/index.html)

[Wikipedia: GIF](https://en.wikipedia.org/wiki/GIF)

### See you on next project:
> _Signing off - [vishal](https://www.instagram.com/r.vishalvimal/)_.

 

