# Segment anything extension

[Segment Anything](https://segment-anything.metademolab.com/) is a promptable, generalist
AI model from Meta that is able to segment many different objects from images. This
document explains how to install and run the [QuPath
extension](https://github.com/ksugar/qupath-extension-sam), written by Ko Sugawara.

The installation of this extension requires a few parts:
* the conda package manager via Miniconda or Anaconda
* the [samapi](https://github.com/ksugar/samapi) server
* the QuPath samapi extension

## Installation

### Conda
You can get conda by downloading and installing either:
* [Miniconda](https://www.anaconda.com/download/success?reg=skipped-miniconda)
* [Anaconda](https://www.anaconda.com/download/success?reg=skipped)

If you do not plan to utilize conda much, we recommend sticking to Miniconda as it is a
smaller install.

Please follow the instructions provided on the website above to install.

### SamAPI

The extension requires that a server runs in the background (on your computer) and hosts
the actual Segment Anything model.

1. After installing conda, open the Anaconda Prompt.

2. Create a new conda environment:
   ```bash
   conda create -n samapi -y python=3.12
   conda activate samapi
   ```

3. Install PyTorch and torchvision which are required dependencies:
   ```bash
   python -m pip install "torch==2.7.0" torchvision --index-url https://download.pytorch.org/whl/cu126
   ```

4. If you are on Windows, you also need to install triton:
   ```bash
   python -m pip install triton-windows
   ```

5. Finally, install the ``samapi`` server:
   ```bash
   python -m pip install git+https://github.com/ksugar/samapi.git
   ```

### QuPath extension

1. Launch QuPath (version 0.6.0 or later)

2. Click on **Extensions** &rarr; **Extension Manager**

3. Click on **Manage extension catalogs**

4. Under the _Catalog URL_ field, enter
   ``https://github.com/ksugar/qupath-catalog-ksugar``. Click on **Add**

5. Close the catalog window. 

6. In the main Extension Manager window, scroll down to the ``QuPath catalog ksugar``
   section.

7. Click on the green plus symbol to install the extension.

## Usage

### Start the ``samapi`` server

1. Launch the Anaconda prompt.

2. In the prompt, activate the ``samapi`` environment and run the server:
   ```bash
   conda activate samapi
   python -m uvicorn samapi.main:app --workers 2
   ```

   ```{important}
   You must leave this window open and running while you use the SAM extension. If you close it on accident, you can simply restart it.
   ```

### Using the QuPath extension

1. Launch QuPath.

2. Launch the extension by clicking on **Extensions** &rarr; **SAM**.

3. Segment Anything is a _promptable_ model, which means that you need to provide either
   rectangles or points for it to segment objects. You can provide prompts by either:

   a. Draw rectangles (R) in QuPath around your objects of interest. You can add
   multiple annotations, then select them in the **Annotations** tab before clicking on
   **Run for selected**.
   b. Place points (.) in QuPath within your objects. You can add multiple points, but
   only one object will be segmented when you click **Run for selected**.








