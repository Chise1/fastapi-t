(function () {
    let amis = amisRequire('amis/embed');
    // 通过替换下面这个配置来生成不同页面
    let amisScoped = amis.embed('#root', {
        "type": "page",
        "body": [{
            "type": "crud",
            "api": "http://127.0.0.1:8000/amis/message",
            "columns": [{"name": "id", "label": "Id"}, {"name": "info", "label": "Info"}, {"name": "e", "label": "E"}],
            "affixHeader": false
        }, {
            "type": "action",
            "label": "\u65b0\u589e",
            "actionType": "dialog",
            "icon": null,
            "size": "md",
            "level": "primary",
            "tooltip": null,
            "dialog": {
                "title": "\u65b0\u589e",
                "body": {
                    "type": "form",
                    "controls": [{
                        "name": "info",
                        "label": "Info",
                        "type": "text",
                        "size": "md",
                        "placeholder": null,
                        "labelRemark": null,
                        "disableOn": null,
                        "hidden": false,
                        "required": true
                    }, {
                        "name": "e",
                        "label": "E",
                        "type": "text",
                        "size": "md",
                        "placeholder": null,
                        "labelRemark": null,
                        "disableOn": null,
                        "hidden": false,
                        "required": true
                    }],
                    "name": "message_create",
                    "title": "\u8868\u5355",
                    "submitText": "\u63d0\u4ea4",
                    "wrapWithPanel": true,
                    "api": "http://127.0.0.1:8000/amis/message",
                    "initApi": null,
                    "primaryField": "id"
                },
                "nextCondition": true,
                "size": "md",
                "actions": null
            }
        }]
    })
})();
