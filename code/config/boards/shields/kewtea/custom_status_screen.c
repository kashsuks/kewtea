/**
 * @file custom_status_screen.c
 * @brief OLED status screen for the kewtea keyboard.
 *
 * Displays elapsed uptime formatted as HH:MM:SS on the 128×32 SSD1306 panel.
 *
 * A hardware RTC (e.g. DS3231) or a host-sync protocol would be required for
 * true wall-clock time. Until one is available, Zephyr's monotonic uptime
 * counter is the only time source on this board.
 */

#include <zephyr/kernel.h>
#include <lvgl.h>
#include <zmk/display.h>

static lv_obj_t *time_label;

/**
 * @brief Converts milliseconds of uptime into HH:MM:SS and updates the label.
 *
 * @param uptime_ms  Monotonic uptime in milliseconds from k_uptime_get().
 */
static void render_uptime(int64_t uptime_ms) {
    const int total_s = (int)(uptime_ms / 1000LL);
    const int hours   = total_s / 3600;
    const int minutes = (total_s % 3600) / 60;
    const int seconds = total_s % 60;

    lv_label_set_text_fmt(time_label, "%02d:%02d:%02d", hours, minutes, seconds);
}

/**
 * @brief LVGL periodic timer callback — fires every 1 000 ms to refresh the time.
 *
 * @param timer  Handle to the triggering LVGL timer (unused).
 */
static void on_tick(lv_timer_t *timer) {
    ARG_UNUSED(timer);
    render_uptime(k_uptime_get());
}

/**
 * @brief Constructs and returns the custom OLED status screen.
 *
 * Called once by ZMK's display subsystem at boot. Creates a single centred
 * Montserrat-16 label showing the current uptime, then schedules a 1 s LVGL
 * timer to keep it updated.
 *
 * @return  Pointer to the root LVGL screen object.
 */
lv_obj_t *zmk_display_status_screen(void) {
    lv_obj_t *screen = lv_obj_create(NULL);

    time_label = lv_label_create(screen);
    lv_obj_set_style_text_font(time_label, &lv_font_montserrat_16, LV_PART_MAIN);
    lv_obj_align(time_label, LV_ALIGN_CENTER, 0, 0);
    lv_label_set_text(time_label, "00:00:00");

    lv_timer_create(on_tick, 1000, NULL);

    return screen;
}
