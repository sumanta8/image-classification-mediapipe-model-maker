# Mediapipe Model Maker Environment Setup Guide

This guide provides step-by-step instructions to set up a TensorFlow environment with MediaPipe Model Maker support.

## Prerequisites

- **Anaconda/Miniconda** installed
- **CUDA-compatible GPU** (recommended)
- Sufficient disk space

## Environment Setup

1. **Create and activate a new Conda environment:**
    ```bash
    conda create -n tf-env python=3.11.9
    conda activate tf-env
    ```

2. **Install ipykernel (if prompted):**
    ```bash
    conda install ipykernel
    ```

3. **Remove existing TensorFlow installations:**
    ```bash
    conda remove tensorflow
    pip uninstall tensorflow
    ```

4. **Install TensorFlow 2.14.0 with CUDA support:**
    ```bash
    conda install tensorflow[and-cuda]==2.14.0
    ```

5. **Clean up TensorFlow-related packages:**
    ```bash
    pip uninstall -y tensorboard tensorboard_data_server tensorflow-addons tensorflow-datasets \
      tensorflow-estimator tensorflow-hub tensorflow-io-gcs-filesystem tensorflow-metadata \
      tensorflow-model-optimization tensorflow-text tf-models-official
    ```

6. **Install MediaPipe Model Maker and dependencies:**
    ```bash
    conda install mediapipe-model-maker
    pip install --no-deps mediapipe-model-maker
    pip install tf-models-official==2.14
    pip install tensorflow_addons
    ```

## Notes

- Python version is **3.11.9**
- TensorFlow version is **2.14.0**
- All conflicting TensorFlow dependencies are removed before installation
- MediaPipe Model Maker is installed without dependencies to avoid version conflicts
- `tf-models-official` is pinned to version **2.14** for compatibility