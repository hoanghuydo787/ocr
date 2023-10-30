import subprocess
import os

input_pattern = sys.argv[1] + "*"
output = sys.argv[2]

for f in glob.glob(input_pattern):
    fname = os.path.basename(f)
    print(f, output + fname)

    imgtxtenh_cmd = [
        "./lib/imgtxtenh",
        "-d", "118.100",
        f
    ]

    convert_cmd = [
        "convert",
        "png:-",
        "-deskew", "40%",
        "-bordercolor", "white",
        "-border", "5",
        "-trim",
        "-strip",
        output + fname
    ]

    imgtxtenh_process = subprocess.Popen(imgtxtenh_cmd, stdout=subprocess.PIPE)
    convert_process = subprocess.Popen(convert_cmd, stdin=imgtxtenh_process.stdout)

    imgtxtenh_process.wait()
    convert_process.wait()
