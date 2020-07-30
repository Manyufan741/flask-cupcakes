const URL = "http://127.0.0.1:5000/api/cupcakes"

class Cupcake {
    constructor(id) {
        this.id = id;
    }

    static generateCupcakeData(cupcake) {
        let $newTr = $('<tr>');
        $newTr.append(`<td style="display:none;">${cupcake.id}</td>`);
        $newTr.append(`<td>${cupcake.flavor}</td>`);
        $newTr.append(`<td>${cupcake.size}</td>`);
        $newTr.append(`<td>${cupcake.rating}</td>`);
        $newTr.append(`<td><img src="${cupcake.image}" width=160 height=200></td>`);
        $newTr.append(`<td><button id="update-btn">Update</button></td>`);
        $newTr.append(`<td><button id="delete-btn">Delete</button></td>`);
        return $newTr;
    }

    static async fetchAllCupcakes() {
        $('#cupcake-table').find("tr:gt(0)").remove();
        const response = await axios.get(`${URL}`);

        for (let cupcake of response.data.cupcakes) {
            let newCupcakeTd = this.generateCupcakeData(cupcake);
            $('#cupcake-table').append(newCupcakeTd);
        }
    }

    static async createCupcakes(data) {
        const response = await axios.post(`${URL}`, data);
    }

    async getCupcake() {
        const response = await axios.get(`${URL}/${this.id}`);
    }

    async updateCupcake(data) {
        const response = await axios.patch(`${URL}/${this.id}`, data);
    }

    async deleteCupcake() {
        const response = await axios.delete(`${URL}/${this.id}`);
    }

}

$('#show-form-btn').on("click", function () {
    $('#add-form').show();
    $('#show-form-btn').hide();
})

$('#add-btn').on("click", function (evt) {
    $('#show-form-btn').show();
    let data = { "flavor": $('#flavor').val(), "size": $('#size').val(), "rating": $('#rating').val(), "image": $('#image').val() };
    Cupcake.createCupcakes(data);
    $('#add-form').hide();
    Cupcake.fetchAllCupcakes();
})

$('#cancel-btn').on("click", function (evt) {
    $('#show-form-btn').show();
    $('#add-form').hide();
    $(':input').val('');
})

let target_id = 0;

$('#cupcake-table').on("click", function (evt) {
    evt.preventDefault();
    let $target = $(evt.target);
    if ($target.text() === "Delete") {
        let id = $target.parent().siblings().first().text();
        let deletedCupcake = new Cupcake(id);
        deletedCupcake.deleteCupcake();
        Cupcake.fetchAllCupcakes();
    }

    if ($target.text() === "Update") {
        $('#table-container').hide();
        target_id = $target.parent().siblings().first().text();
        console.log('target-id', target_id);
        $('#update-form').show();
    }
})

$('#update-save-btn').on("click", async function (evt) {
    evt.preventDefault();
    let data = { "flavor": $('#update_flavor').val(), "size": $('#update_size').val(), "rating": $('#update_rating').val(), "image": $('#update_image').val() };
    let cupcake = new Cupcake(target_id);
    console.log('data', data);
    console.log('id', target_id);
    cupcake.updateCupcake(data);
    $('#update-form').hide();
    Cupcake.fetchAllCupcakes();
    $('#table-container').show();
})

$('#update-cancel-btn').on("click", function () {
    $('#update-form').hide();
    // $(':input').val('');
    $('#table-container').show();
})