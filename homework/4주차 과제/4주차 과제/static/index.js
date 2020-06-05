function make_review() {
    // 1. 제목, 저자, 리뷰 내용을 가져옵니다.
    let title = $('#name').val();
    let author = $('#quantity').val();
    let review = $('#address').val();
    let tel = $('#telephone').val();

    // 2. 제목, 저자, 리뷰 중 하나라도 입력하지 않았을 경우 alert를 띄웁니다.
    if (title == '') {
        alert('제목을 입력해주세요');
        $('#title').focus();
        return;
    } else if (author == '') {
        alert('수량을 입력해주세요');
        $('#quantity').focus();
        return;
    } else if (review == '') {
        alert('주소를 입력해주세요');
        $('#address').focus();
        return;
    } else if (tel == '') {
        alert('번호를 입력해주세요');
        $('#telephone').focus();
        return;
    }

    alert(title + " " + author + " " + review + " " + tel)
        // 3. POST /reviews 에 저장을 요청합니다.
    $.ajax({
        type: "POST",
        url: "/order",
        data: {
            title_give: title,
            author_give: author,
            review_give: review,
            tel_give: tel
        },
        success: function(response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                window.location.reload();
            }
        }
    })
}
$(document).ready(function() {
    listing();
});

function listing() {
    // 1. 리뷰 목록을 서버에 요청하기
    $.ajax({
        type: "GET",
        url: "/order",
        data: {},
        success: function(response) {
            // 2. 요청 성공 여부 확인하기
            if (response['result'] == 'success') {
                let orders = response['order'];
                // 3. 요청 성공했을 때 리뷰를 올바르게 화면에 나타내기
                for (let i = 0; i < orders.length; i++) {
                    make_card(orders[i]['title'], orders[i]['author'], orders[i]['review'], orders[i]['tel']);
                }
            } else {
                alert('리뷰를 받아오지 못했습니다');
            }
        }
    })
}


function make_card(title, author, review, tel) {
    let temp_html = `<tr>
                <td>${title}</td>
                <td>${author}</td>
                <td>${review}</td>
                <td>${tel}</td>
            </tr>`;
    $('#orders-box').append(temp_html);
}