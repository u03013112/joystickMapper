# joystickMapper
手柄映射到键盘

最近Ryujinx出了针对M1的版本，正好公司提供的工作设备是M1 pro~
在玩ns模拟器的时候，发现一般的手柄并不受模拟器兼容，根本不识别。只能键盘的ns不是想要的ns。

尝试将手柄映射到键盘，这种项目之前有一些，比如enjoyable，效果不好，需要sudo才能有效的使用，另外，他造成了口袋妖怪游戏异常，包括但不仅限于游戏中商店不能对话，不能存档，不能战斗中选择不同招式。经过确认，通过键盘来玩的时候确实没有出现。所以我觉得大概率是键盘映射者造成的，但是那个是好多年以前的oc写的，很多api都废弃了，也不好调试。

所以决定用py写一个简单的自己先用。