let test = null
const updateTree = (data) => {
    $('#tree').empty()
    $('#treeUpdate').html('<div id="tree"/>')
    $('#tree').bstreeview({
        data: data.tree.cats
    });
}
let contextMenu = {
    id: 'CONTEXT-MENU',
    data: [
        {header: 'Меню'},
        {
            icon: 'glyphicon-plus',
            text: 'Удалить категорию',
            action: function(e, selector) { deleteCategory(test) }
        },
    ]
}

const deleteCategory = (pk) => {

    let arr  = $('#category_form').serializeArray()
    arr.pop()
    $.ajax({
        url: '/delete_category/'+ pk,
        type: 'post',
        dataType: "json",
        data: arr,
        success: (result) => {
            updateTree(result)
            clickElem()
            context.attach('#tree', contextMenu);
            $.toast({ heading: 'Внимание!',  text: result.msg,  icon: 'info',  position: 'mid-center',  stack: false })
        }
    });
}

const clickElem = () => {
    $('#tree').mousedown(function(e){
        if( e.button === 2 ) {
            $('#liveToast').toggle("slow" )

            test = e.target.id
            return false
        } else if (e.button === 0)
        {
            let cat_id = e.target.id
            $('#cat_name').html(e.target.textContent)
            $('#cat_id').html(cat_id)
            return false;
        }
        return true;
    });
}

const check_edit_cat = () => {
    $('#cat_btn').on('click', function (){
        $('#block_cat').show()
        $('#block_elem').hide()
    })
}

const check_edit_elem = () => {
    $('#elem_btn').on('click', function (){
        $('#block_cat').hide()
        $('#block_elem').show()
    })
}

/////////For Pass Reestr///////

const getElems = () => {
    $('#tree').on('click', function(e){
        let parent_id = e.target.id
        if (parent_id !== '') {
            document.location.href = '/pass_reestr/'+ parent_id
        }
    })
}


const getIdElem = () => {
    $('#elems').mousedown(function(e){
        if( e.button === 2 ) {
            elemId = e.target.id
        }
    })
}

const decrypt_result = (result) => {
     $('#id_login').val(result.data.login)
                $('#create_elem').attr('action', '/update_elem/'+ result.data.pk + '/')
                $('#id_password').attr('type','input')
                $('#id_password').val(result.data.password)
                $('#id_description').val(result.data.description)
}

const getCSRFToken = () => {
         const cookieValue = document.cookie.split(';')
            const re = /csrftoken=\S*/
            let csrfToken = ''
                cookieValue.filter(function (item) {
                if (item.match(re) !== null) {
                  csrfToken = item.split('=')[1]
                }
            })
    return csrfToken
}

const getDecryptElems = (pk) => {
    if(pk !== ''){
        if (checkSettings()) {
            const csrfToken = getCSRFToken()
            const data = {key: sessionStorage.getItem('keyPass'), csrfmiddlewaretoken: csrfToken}
            ajaxRequest(data, '/decrypt_elem/'+ pk+'/', decrypt_result)
        } else {
             $.toast({ heading: 'Внимание!',  text: 'Выполни настройку дружок!',  icon: 'warning',
                           position: 'mid-center',  stack: false })
        }

    }
}

//// Settings pass ya disk
class YaDisk {
    constructor() {
        this.card =  $('#card_code')
        this.msg = $('#msg')
        this.yaToken = sessionStorage.getItem('yaToken')
        this.csrf = $("[name='csrfmiddlewaretoken']").val()
        this.checkToken()
    }
    checkToken(){
       this.card.hide()
        if (this.yaToken === null) {
            this.msg.show()
        } else {
             this.msg.hide()
        }
    }
    postCode(){
        $.ajax({
            url: $('#urlCode').val(),
            type: 'post',
            dataType: 'JSON',
            data: {'csrfmiddlewaretoken': this.csrf, 'code': $('#inp_code').val()},
            success: (result) => {
                  if (result.data.status === 'url') {
                    window.open(result.data.msg, '_blank');
                    this.card.show()
                    this.msg.hide()
                } else if (result.data.status === 'token') {
                      sessionStorage.setItem('yaToken', result.data.msg)
                       $.toast({ heading: 'Ответ!',  text: 'Токен получен!',  icon: 'info',
                           position: 'mid-center',  stack: false })
                      this.card.hide()
                      this.msg.hide()
                  }
                  else {
                       $.toast({ heading: 'Ошибка!',  text: result.data.msg,  icon: 'error',
                           position: 'mid-center',  stack: false })
                  }
            }
        })
    }

    syncYaDisk() {
        this.yaToken = sessionStorage.getItem('yaToken')
        $.ajax({
            url: $('#urlYa').val(),
            type: 'post',
            dataType: 'JSON',
            data: {'csrfmiddlewaretoken': this.csrf, 'token': this.yaToken},
            success: (result) => {
                if (result.data.status === 'url') {
                    window.open(result.data.msg, '_blank');
                    this.card.show()
                    this.msg.hide()
                }
                else if (result.data.status === 'ok') {
                    $.toast({ heading: result.data.status,  text: result.data.msg,  icon: 'success',
                           position: 'mid-center',  stack: false })
                }
                else {
                    $.toast({ heading: 'Ошибка!',  text: result.data.msg,  icon: 'error',
                           position: 'mid-center',  stack: false })
                }
            }
        })
    }
}

const ajaxRequest = (data, url, workFunc) => {
     $.ajax({
            url: url,
            type: 'post',
            dataType: 'JSON',
            data: data,
            success: (result) => {
                workFunc(result)
            }
        })
}

class Encryption {
    constructor(msg) {
        this.keyPass = sessionStorage.getItem('keyPass')
        this.msgKey = $('#msg_check_key')
        this.checkKeyPass(msg)
    }

    checkKeyPass(msg) {
        if (this.keyPass !== null) {
            if (msg.key_id !== ''){
                sessionStorage.setItem('keyId', msg.key_id)
                this.msgKey.attr('style' , 'color: #337B0CE6')
                this.msgKey.children().html('Все настройки применены успешно!')
            } else {
                sessionStorage.removeItem('keyPass')
            }

        }
    }

    postKeyPass(result) {
        if (result.status === 'ok') {
            sessionStorage.setItem('keyPass', result.passKey)
        location.reload()
        } else {
             $.toast({ heading: 'Ошибка!', text: result.msg,  icon: 'error',
                           position: 'mid-center',  stack: false })
        }

    }
}

const checkSettings = () => {
    const keyPass = sessionStorage.getItem('keyPass')
    const keyId = sessionStorage.getItem('keyId')
    return keyId!==null && keyPass!==null
}
//Функция для удаление эелементов (там где есть модальное окно)
const deleteElems = (url) => {
     $('#delete_act').attr('action', url)
     $('#deleteModal').modal('toggle')
}