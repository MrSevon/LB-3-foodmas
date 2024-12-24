document.addEventListener("DOMContentLoaded", function () {
    const sliderMin = document.getElementById("slider-min");
    const sliderMax = document.getElementById("slider-max");
    const inputMin = document.getElementById("price-min-input");
    const inputMax = document.getElementById("price-max-input");
    const hiddenMin = document.getElementById("hidden-price-min");
    const hiddenMax = document.getElementById("hidden-price-max");
    const filterForm = document.getElementById("filter-form");

    function updateInputs() {
        inputMin.value = sliderMin.value;
        inputMax.value = sliderMax.value;
        hiddenMin.value = sliderMin.value;
        hiddenMax.value = sliderMax.value;
    }

    function updateSliders() {
        sliderMin.value = inputMin.value;
        sliderMax.value = inputMax.value;
    }

    function validateSliders() {
        let minValue = parseInt(sliderMin.value);
        let maxValue = parseInt(sliderMax.value);

        if (minValue >= maxValue) {
            sliderMin.value = maxValue - 1;
        }

        if (maxValue <= minValue) {
            sliderMax.value = minValue + 1;
        }

        updateInputs();
    }

    function submitForm() {
        hiddenMin.value = sliderMin.value;
        hiddenMax.value = sliderMax.value;
        filterForm.submit();
    }

    sliderMin.addEventListener("input", () => {
        validateSliders();
    });

    sliderMax.addEventListener("input", () => {
        validateSliders();
    });

    sliderMin.addEventListener("change", submitForm);
    sliderMax.addEventListener("change", submitForm);

    inputMin.addEventListener("change", () => {
        if (parseInt(inputMin.value) >= parseInt(sliderMax.value)) {
            inputMin.value = parseInt(sliderMax.value) - 1;
        }
        updateSliders();
        submitForm();
    });

    inputMax.addEventListener("change", () => {
        if (parseInt(inputMax.value) <= parseInt(sliderMin.value)) {
            inputMax.value = parseInt(sliderMin.value) + 1;
        }
        updateSliders();
        submitForm();
    });

    document.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
        checkbox.addEventListener("change", submitForm);
    });

    updateInputs();
});
