package com.autulin.reportlaniptoremote;

import lombok.Getter;
import lombok.Setter;

import javax.validation.constraints.NotNull;
import java.util.Date;

@Getter
@Setter
public class IpRecord {
    @NotNull
    private String ip;
    private Date date;
}
