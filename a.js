(function () {
let amis = amisRequire('amis/embed');
// 通过替换下面这个配置来生成不同页面
let amisScoped = amis.embed('#root',{
  "type": "page",
  "body": {
    "type": "hbox",
    "className": "b-a m-t lter",
    "columns": [
      {
        "type": "nav",
        "stacked": true,
        "className": "w-md",
        "columnClassName": "w-md wrapper-xs bg-primary b-r",
        "links": [
          {
            "label": "Nav 1",
            "to": "/docs/index",
            "icon": "fa fa-user",
            "active": true
          },
          {
            "label": "Nav 2",
            "unfolded": true,
            "children": [
              {
                "label": "Nav 2-1",
                "children": [
                  {
                    "label": "Nav 2-1-1",
                    "to": "/docs/api-2-1-1"
                  }
                ]
              },
              {
                "label": "Nav 2-2",
                "to": "/docs/api-2-2"
              }
            ]
          },
          {
            "label": "Nav 3",
            "to": "/docs/renderers"
          }
        ]
      },
      {
        "type": "page",
        "name":"basepage",
        "body": [
          {
            "type": "panel",
            "title": "面板标题",
            "body": "面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa面板内容egraaaaaaaaaaaaa",
            "affixFooter": true,
            "actions": [
              {
                "type": "button",
                "label": "按钮 1",
                "actionType": "dialog",
                "dialog": {
                  "title": "提示",
                  "body": "对，你刚点击了！"
                }
              },
              {
                "type": "button",
                "label": "按钮 2",
                "actionType": "dialog",
                "dialog": {
                  "title": "提示",
                  "body": "对，你刚点击了！"
                }
              }
            ]
          },
          {
            "type": "text",
            "body": "我是第二个面板"
          }
        ]
      }
    ]
  }
},{},{
    jumpTo:location=>{
        fetch(location,{
            method: 'get'
        }).then((res) => {
            return res.json()
        }).then((res) => {
            amisScoped.getComponentByName("basepage.body").setValues(res)
        })
    }
})})();