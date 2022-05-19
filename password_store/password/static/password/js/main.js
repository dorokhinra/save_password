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

  const getDecryptElems = (pk) => {
        if(pk !== ''){
           $.ajax({
                url: '/decrypt_elem/'+ pk+'/',
                type: 'get',
                success: (result) => {
                    $('#id_login').val(result.data.login)
                    $('#id_password').attr('type','input')
                    $('#id_password').val(result.data.password)
                    $('#id_description').val(result.data.description)
                    console.log(result)                }
            });
        }
}