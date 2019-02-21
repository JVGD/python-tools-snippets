from lxml import etree


in_path = "/home/jvgd/datasets/fake_out_ds/train_annot/"
filename = "00011db7-3e79-4fa9-b3a0-5e6b152a41f0.xml"
new_path = "./my/custom/folder/path/custom"


# Start
file = in_path + filename

# annot
# Getting XML tree in c_annot
xml_file = etree.parse(file)

# Getting folders in the element tree XML using xpath
# and rewriting the folder attribute with the new path
# for the processed image
# annotation <annotation> .. <folder> ../datasets/..</folder>
for c_img_folder in xml_file.xpath("/annotation/folder"):
    # Change folder of the annotation to the new folder
    c_img_folder.text = new_path

# Once folder field is renamed we write it and count it
xml_file.write(file)


print("Done!")
print("cat " + file + " | xmllint --format -")