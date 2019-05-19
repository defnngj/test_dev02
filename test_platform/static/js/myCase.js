//创建下拉选项
function cmbAddOption(cmb, obj) {
    let option = document.createElement("option");
    cmb.options.add(option);
    option.innerHTML = obj.name;
    option.value = obj.id;
}

//清理下拉选项
function clearOption(cmb) {
    for (let i = 0; i <= cmb.length; i++) {
        cmb.options.remove(cmb[i]);
    }
}


// 获取项目列表
var ProjectInit = function (_cmbProject, defaultId) {
    var cmbProject = document.getElementById(_cmbProject);
    
    console.log("defaultId--->", defaultId);

    function getProjectListInfo() {
        $.get("/project/get_project_list/", {}, function (resp) {
            if (resp.status == 10200) {
                console.log(resp.data);
                let dataList = resp.data;
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbProject, dataList[i]);
                }
            } else {
                window.alert(resp.message);
            }
        });
    }

    // 调用getCaseListInfo函数
    getProjectListInfo();
    
    //document.getElementById("sel")[2].selected = true;
    
    
};


// 获取某一个项目的模块列表
var ModuleInit = function (_cmbModule, pid) {
    var cmbModule = document.getElementById(_cmbModule);

    function getModuleListInfo() {
        $.post("/module/get_module_list/", {
            "pid": pid
        }, function (resp) {
            if (resp.status == 10200) {
                console.log(resp.data);
                let dataList = resp.data;
                clearOption(cmbModule);
                for (let i = 0; i < dataList.length; i++) {
                    cmbAddOption(cmbModule, dataList[i]);
                }
                $("#module_name").selectpicker("refresh");
            } else {
                window.alert(resp.message);
            }
        });
    }

    // 调用getCaseListInfo函数
    getModuleListInfo();

};


var SelectModule = function (mid) {
    
        let options2 = document.querySelectorAll("#module_name > option");
        console.log("bbbb", options2.length);
        for (let i = 0; i < options2.length; i++) {
            let v2 = options2[i].value;
            if (v2 == mid) {
                console.log("所属模块的id---》", v2);
                options2[i].selected = true;
                let text = options2[i].text;
                console.log("所属的模块名称---》", text);
                document.querySelectorAll(".filter-option-inner-inner")[1].innerText = text;
            }

        }
}

//获取用例信息
var TestCaseInit = function () {

    var url = document.location;
    var cid =  url.pathname.split("/")[3];

    $.post("/testcase/get_case_info",
    {
        cid: cid,
    },
    function (resp, status) {
        console.log("返回的结果", resp.data);
        
        //url
        document.querySelector("#req_url").value = resp.data.url;
        
        // 请求方法
        if (resp.data.method == 1){
            document.querySelector("#get").setAttribute("checked", "");
        }
        else if (resp.data.method == 2) {
            document.querySelector("#post").setAttribute("checked", "");
        }
        //请求头
        document.querySelector("#header").value = resp.data.header;

        //请求参数类型
        if (resp.data.parameter_type == 1) {
            document.querySelector("#form").setAttribute("checked", "");
        }
        else if (resp.data.parameter_type == 2) {
            document.querySelector("#json").setAttribute("checked", "");
        }

        //请求参数的值
        document.querySelector("#parameter").value = resp.data.parameter_body;
        
        //断言的类型
        if (resp.data.assert_type == 1) {
            document.querySelector("#contains").setAttribute("checked", "");
        }
        else if (resp.data.assert_type == 2) {
            document.querySelector("#mathches").setAttribute("checked", "");
        }

        //断言的值
        document.querySelector("#assert").value = resp.data.assert_text;

        //用例的名称
        document.querySelector("#case_name").value = resp.data.name;

        let options = document.querySelectorAll("#project_name > option");
        console.log("aaaa", options.length);
        for (let i = 0; i < options.length; i++) {
            let v = options[i].value;
            if (v == resp.data.project_id){
                console.log("所属的项目id---》", v);
                options[i].selected = true;
                let text = options[i].text;
                console.log("所属的项目名称---》", text);
                document.querySelectorAll(".filter-option-inner-inner")[0].innerText = text;
            }
        }

        ModuleInit("module_name", resp.data.project_id);

        SelectModule(resp.data.module_id);

    });
    
}