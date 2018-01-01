Django上传文件
--------------
*遇到的问题*

* 有关form的一切代码应记录在forms.py文件中，与models.py相似

* 继承forms.Form的类，可以被渲染成表单元素<input>

* form子类的初始化传入HttpRequest.POST和HttpRequest.FILES的实例，
前者（字典）是与Form类的字段相关（表单元素的name属性），后者（字典）
与上传的文件本身相关，可通过request.FILES['file']   :code:`file` 指FileField成员

* 表单method=Post，设计HTML时应在form元素内加入 :code:`{% csrf_token %}`

* 上传文件的form表单注意两点 :code:`method=Post`以及:code:`enctype="multipart/form-data"`


总结
^^^^
考虑将博客渲染部分由Markdown改为restructuredtext,直接上传restructuredtext格式的文件可以被渲染和显示。