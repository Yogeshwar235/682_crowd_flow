## Setup

1. Clone the repository
2. install conda 
3. create a new conda environment with the following command:
```bash
conda create --name compsci682 --file requirements.txt
```
4. activate the environment with the following command:
```bash
conda activate compsci682
```
5. Download the dataset using the following command:
```bash
python scripts/download_datasets.py

cat tmp/682_proj_datasets.tar.zst.part_0* > tmp/682_proj_datasets.tar.zst

shasum -c 682_proj_datasets-CHECKSUM tmp682_proj_datasets.tar.zst

# if zstd is not installed, install it using the following command

brew install zstd

tar --zstd -xf tmp/682_proj_datasets.tar.zst

```



## Running the code

Use Jupiter notebook to run the code. The code is divided into 3 parts:
1. Data Preprocessing
2. Training
3. Testing
