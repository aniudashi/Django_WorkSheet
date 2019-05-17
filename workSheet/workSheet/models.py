from django.db import models

class workSheetTable(models.Model):
    TOPIC_TYPE_CHOICE = (
        ('D', '需求'),
        ('B', '问题'),
        ('P', '疑问'),
    )
    DEV_STATE_CHOICE = (
        ('U', '未开发'),
        ('I', '开发中'),
        ('D', '开发完成'),
        ('A', '待分析'),
    )
    TEST_STATE_CHOICE = (
        ('U', '未测试'),
        ('I', '测试中'),
        ('D', '测试完成'),
    )
    priority = models.IntegerField('优先级')
    order_id = models.IntegerField('序号ID')
    order_time = models.DateField('提出时间')
    topic_desc = models.CharField('需求/问题描述',max_length=1000)
    topic_type = models.CharField('类型',max_length=10,choices=TOPIC_TYPE_CHOICE,default='D')
    topic_desc = models.CharField('备注',max_length=1000)
    dev_person = models.CharField('开发人员',max_length=16)
    dev_state = models.CharField('开发状态',max_length=10,choices=DEV_STATE_CHOICE)
    plan_dev_finish_time = models.DateField('计划开发完成时间')
    dev_finish_time = models.DateField('实际开发完成时间')
    test_person = models.CharField('测试人员',max_length=16)
    test_state = models.CharField('测试状态',max_length=16,choices=TEST_STATE_CHOICE)
    plan_test_finish_time = models.DateField('计划测试完成时间')
    test_finish_time = models.DateField('实际测试完成时间')
    plan_online_time = models.DateField('计划上线时间')
    
    def as_dict(self):
        data = {}
        data["priority"] = self.priority
        return d
