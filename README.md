# Run-Mnist-in-the-NPU-of-V851s-Lizard
仓库结构如下：
.
├── MNIST
│   └── raw
│       ├── t10k-images-idx3-ubyte
│       ├── t10k-images-idx3-ubyte.gz
│       ├── t10k-labels-idx1-ubyte
│       ├── t10k-labels-idx1-ubyte.gz
│       ├── train-images-idx3-ubyte
│       ├── train-images-idx3-ubyte.gz
│       ├── train-labels-idx1-ubyte
│       └── train-labels-idx1-ubyte.gz
├── mnist_train.py
├── model
│   ├── data
│   │   ├── test_11_6.jpg
│   │   ├── test_12_9.jpg
│   │   ├── test_13_0.jpg
│   │   ├── test_14_1.jpg
│   │   ├── test_15_5.jpg
│   │   ├── test_16_9.jpg
│   │   ├── test_18_3.jpg
│   │   ├── test_19_4.jpg
│   │   ├── test_20_9.jpg
│   │   ├── test_22_6.jpg
│   │   ├── test_23_5.jpg
│   │   └── test_24_4.jpg
│   ├── dataset.txt
│   ├── iter_0_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_0_input_10_out0_1_1_28_28.tensor
│   ├── iter_10_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_10_input_10_out0_1_1_28_28.tensor
│   ├── iter_11_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_11_input_10_out0_1_1_28_28.tensor
│   ├── iter_1_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_1_input_10_out0_1_1_28_28.tensor
│   ├── iter_2_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_2_input_10_out0_1_1_28_28.tensor
│   ├── iter_3_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_3_input_10_out0_1_1_28_28.tensor
│   ├── iter_4_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_4_input_10_out0_1_1_28_28.tensor
│   ├── iter_5_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_5_input_10_out0_1_1_28_28.tensor
│   ├── iter_6_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_6_input_10_out0_1_1_28_28.tensor
│   ├── iter_7_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_7_input_10_out0_1_1_28_28.tensor
│   ├── iter_8_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_8_input_10_out0_1_1_28_28.tensor
│   ├── iter_9_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor
│   ├── iter_9_input_10_out0_1_1_28_28.tensor
│   ├── mnist.data
│   ├── mnist-inputmeta.yml
│   ├── mnist.json
│   ├── mnist.onnx
│   ├── mnist-postprocess-file.yml
│   ├── mnist.quantilize
│   └── ovxlib
│       ├── mnist
│       └── mnist_nbg_unify
├── pth_to_onnx.py
└── README.md

