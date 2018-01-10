JavaScript
==========

HTML 输出
---------
::

    document.write("<h1>This is a heading</h1>");
    document.write("<p>This is a paragraph</p>");

*转大写*
::
    
    message.toUpperCase()

*定义变量*
::

    var x=message.length;

*定义函数*

::

    function myFunction()
    {
        var x=5;
        return x;
    }

**在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它。**

值比较
------
::

    variablename=(condition)?value1:value2 


文档对象模型（Document Object Model）
------------------------------------
::

    document.getElementById(id).attribute=new value
    
    document.getElementById(id).style.property=new style
    
    document.getElementById("myBtn").onclick=function(){displayDate()};
    
    var para=document.createElement("p");
    
    var element=document.getElementById("div1");
    
    element.appendChild(para);

脚本
----
::

    <script>
    var parent=document.getElementById("div1");
    var child=document.getElementById("p1");
    parent.removeChild(child);
    </script>