import torch
import onnx


class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(1, 10, kernel_size=5),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
        )
        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(10, 20, kernel_size=5),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(kernel_size=2),
        )
        self.fc = torch.nn.Sequential(
            torch.nn.Linear(320, 50),
            torch.nn.Linear(50, 10),
        )

    def forward(self, x):
        batch_size = x.size(0)
        x = self.conv1(
            x
        )  # 一层卷积层,一层池化层,一层激活层(图是先卷积后激活再池化，差别不大)
        x = self.conv2(x)  # 再来一次
        x = x.view(
            batch_size, -1
        )  # flatten 变成全连接网络需要的输入 (batch, 20,4,4) ==> (batch,320), -1 此处自动算出的是320
        x = self.fc(x)
        return x  # 最后输出的是维度为10的，也就是（对应数学符号的0~9）


model = Net()

model.load_state_dict(torch.load("./model_Mnist.pth"))
model.eval()
# 3. 准备虚拟输入
dummy_input = torch.randn(1, 1, 28, 28)
# 4. 导出ONNX
torch.onnx.export(
    model,
    dummy_input,
    "./mnist.onnx",
    input_names=["input"],
    output_names=["output"],
    opset_version=13,
)
# 5. 验证
onnx.checker.check_model(onnx.load("mnist.onnx"))
print("转换成功！")
