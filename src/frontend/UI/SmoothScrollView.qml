import QtQuick
import QtQuick.Controls

ScrollView {
    id: control

    property alias wheelStep: wheelHandler.wheelStep
    property alias wheelAnimationDuration: wheelHandler.animationDuration

    SmoothWheelHandler {
        id: wheelHandler
        flickable: control.contentItem
    }

    ScrollBar.vertical: ScrollBar {
        policy: ScrollBar.AsNeeded
        active: size < 1.0 || hovered || pressed || wheelHandler.scrolling
    }
}
