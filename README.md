# Run-Mnist-in-the-NPU-of-V851s-Lizard

---

## 仓库结构  
.  
├── MNIST  
│   └── raw  
├── mnist_train.py  
├── model  
│   ├── data  
│   ├── dataset.txt  
│   ├── iter_0_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_0_input_10_out0_1_1_28_28.tensor  
│   ├── iter_10_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_10_input_10_out0_1_1_28_28.tensor  
│   ├── iter_11_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_11_input_10_out0_1_1_28_28.tensor  
│   ├── iter_1_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_1_input_10_out0_1_1_28_28.tensor  
│   ├── iter_2_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_2_input_10_out0_1_1_28_28.tensor  
│   ├── iter_3_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_3_input_10_out0_1_1_28_28.tensor  
│   ├── iter_4_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_4_input_10_out0_1_1_28_28.tensor  
│   ├── iter_5_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_5_input_10_out0_1_1_28_28.tensor  
│   ├── iter_6_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_6_input_10_out0_1_1_28_28.tensor  
│   ├── iter_7_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_7_input_10_out0_1_1_28_28.tensor  
│   ├── iter_8_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_8_input_10_out0_1_1_28_28.tensor  
│   ├── iter_9_attach_Gemm__fc_fc.1_Gemm_out0_0_out0_1_10.tensor  
│   ├── iter_9_input_10_out0_1_1_28_28.tensor  
│   ├── mnist.data  
│   ├── mnist-inputmeta.yml  
│   ├── mnist.json  
│   ├── mnist.onnx  
│   ├── mnist-postprocess-file.yml  
│   ├── mnist.quantilize  
│   └── ovxlib  
├── npu  
│   ├── lenet  
│   ├── viplite-driver  
│   ├── vpm_run  
│   └── yolov3  
├── pth_to_onnx.py  
└── README.md

* ./mnist_train.py：MNIST训练代码
* ./pth_to_onnx.py：pytorch模型转换onnx模型代码
    > 本人在使用全志模型转换工具链时无法解决pth的报错问题，故将pth模型转化为onnx模型再进行模型转换
* ./MNIST/raw/：MNIST数据集
* ./npu/：全志V85x系列npu拓展工具包
* ./model/data：模型转换用的部分数据集
* ./model/dataset.txt：模型转换用的部分数据集清单
* ./model/iter_*.tensor：模型转换生成的推理tensor，用于转换后预推理和板上NPU推理
* ./model/ovxlib/：模型转换结果，用于板上NPU推理的模型network_binary.nb存于./model/ovxlib/mnist_nbg_unify/
* __模型在板上NPU推理请参考V853的lenet和vpm_run的例程__

---

## 参考链接
模型转换工具安装：[https://v853.docs.aw-ol.com/npu/npu_dev_startup/](https://v853.docs.aw-ol.com/npu/npu_dev_startup/)  
模型转换：[https://v853.docs.aw-ol.com/npu/npu_yolov3/](https://v853.docs.aw-ol.com/npu/npu_yolov3/)  
NPU推理：[https://v853.docs.aw-ol.com/npu/npu_demo/](https://v853.docs.aw-ol.com/npu/npu_demo/)  