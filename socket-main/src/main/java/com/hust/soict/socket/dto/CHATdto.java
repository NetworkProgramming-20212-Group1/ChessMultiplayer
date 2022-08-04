package com.hust.soict.socket.dto;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class CHATdto {
    private String message;
    private String roomid;
}
